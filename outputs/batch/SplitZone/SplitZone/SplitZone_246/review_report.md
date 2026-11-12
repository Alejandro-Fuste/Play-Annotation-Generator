# Play-Annotation-Generator Annotation Review — SplitZone_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_246`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 23 | START | 24 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 23 | START | 24 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 23 | START | 24 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 23 | START | 24 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 23 | START | 24 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 23 | START | 24 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 23 | START | 24 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 23 | START | 24 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 23 | START | 24 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 95 | START | 95 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 98 | START | 98 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 98 | START | 98 | 197 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 98 | START | 111 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 98 | START | 98 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 98 | START | 98 | 197 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `4` | `4` | 99 | START | 99 | 181 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 110 | END | 95 | 110 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 118 | START | 118 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 130 | START | 130 | 136 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 197 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 24–215
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 129 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 215 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 129 | 106 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 136 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–181
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_SplitBlock` | 99 | 181 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 97 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 197 | 100 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 97 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 197 | 100 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 24–165
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 165 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 97 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 184 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 97 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 197 | 100 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 145 | 19 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 24–158
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 118 | 24 | inferred_complete_timeline |
| `Action_None` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 150 | 158 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 24–144
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 111 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–195
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 195 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 24–235
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 235 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–151
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 147 | 53 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 182 | 88 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 242 | 148 | inferred_complete_timeline |
| `Action_None` | 245 | 259 | 15 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_None` | 95 | 205 | 111 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 125–299 | 163 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 154–299 | 130 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 167–285 | 119 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 186–219 | 34 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 193–299 | 102 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 204–299 | 94 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 217–221 | 4 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 230–299 | 70 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 98 != Inferred start 111
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [95–110], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=111.
- ⚠️ Action 'Action_ZoneBlock' range [98-184] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 198, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [198-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 198, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [198-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [99-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-299] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-299] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>