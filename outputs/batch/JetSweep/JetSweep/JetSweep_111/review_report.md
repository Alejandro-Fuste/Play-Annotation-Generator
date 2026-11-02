# Play-Annotation-Generator Annotation Review — JetSweep_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_111`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 76 | START | 76 | 90 |
| ✅ EXACT | `Action_LeadBlock` | RB | `12` | `11` | 78 | START | 78 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 78 | START | 78 | 123 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 78 | START | 91 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 78 | START | 78 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 78 | START | 78 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 78 | START | 78 | 177 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 84 | START | 84 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 90 | END | 76 | 90 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 95 | START | 95 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 111 | START | 111 | 201 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_Toss` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 131 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_LeadBlock` | 78 | 169 | 92 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 162 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 177 | 1 | inferred_complete_timeline |
| `Action_None` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 109 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 136 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 160 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 177 | 87 | inferred_complete_timeline |
| `Action_None` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 123 | 46 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 177 | 100 | inferred_complete_timeline |
| `Action_None` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 231 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 95 | 20 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 107 | 32 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 175 | 58 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 146 | 71 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 173 | 98 | inferred_complete_timeline |
| `Action_None` | 175 | 190 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 97 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 108 | 33 | inferred_complete_timeline |
| `Action_None` | 114 | 165 | 52 | inferred_complete_timeline |
| `Action_None` | 170 | 182 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 209 | 9 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 237 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–220 | 207 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 84–221 | 122 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 129–137 | 9 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 132–181 | 50 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 134–176 | 31 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 195–239 | 32 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 202–239 | 38 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 78 != Inferred start 91
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '11' (RB) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 100 frames exceeds threshold 90 frames [start=78, end=177].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [76–90], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=91.
- ⚠️ Action 'Action_None' range [76-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-239] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-163] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-162] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-146] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-231] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-177] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 178, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [178-184] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [78-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>