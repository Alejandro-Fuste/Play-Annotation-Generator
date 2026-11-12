# Play-Annotation-Generator Annotation Review — SplitZone_191

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_191`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 5
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LT | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 17 | START | 18 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 17 | START | 18 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 17 | START | 18 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 17 | START | 18 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 17 | START | 18 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 17 | START | 18 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 17 | START | 18 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 17 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 17 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 17 | START | 18 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 17 | START | 18 | 141 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 110 | START | 110 | 117 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 113 | START | 133 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 113 | START | 113 | 117 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `15` | `15` | 113 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `19` | `19` | 113 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `21` | `21` | 113 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `1` | `1` | 121 | START | 121 | 160 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 125 | END | 110 | 125 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 135 | START | 135 | 141 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `8` | 142 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LT | `19` | `19` | 147 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 18–255
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_None` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 255 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–141
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 141 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 230 | 121 | inferred_complete_timeline |
| `Action_None` | 236 | 246 | 11 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–207
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 120 | 103 | inferred_complete_timeline |
| `Action_SplitBlock` | 121 | 160 | 40 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 199 | 35 | inferred_complete_timeline |
| `Action_SplitBlock` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–54
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 18–56
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 56 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 18–134
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_BallSnap` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 18–54
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–268
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 84 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 128 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 265 | 27 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 18–55
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 55 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 18–120
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 106 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 109 | 1 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 18–54
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–170
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 165 | 56 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–153
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 153 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 18–253
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 253 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 18–269 | 246 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 152–256 | 100 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 162–177 | 15 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 169–173 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 187–269 | 71 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 198–209 | 12 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 199–207 | 9 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 208–269 | 61 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 214–258 | 7 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 231–269 | 35 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 231–234 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 238–249 | 12 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 241–269 | 29 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 243–252 | 10 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 252–269 | 13 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 254–257 | 4 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 257–267 | 11 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 113 != Inferred start 133
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `1` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `19` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '8' has invalid range: start=142, end=141. Clamping end to start.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [110–125], lower_priority='Action_ZoneBlock' annotated_start=113, effective_Action_ZoneBlock_start=126.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 105 frames exceeds threshold 90 frames [start=113, end=217].
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=113, end=56. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=113, end=54. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '19' has invalid range: start=147, end=54. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=113, end=54. Clamping end to start.
- ⚠️ Action 'Action_None' range [110-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [121-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [165-199] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [205-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-205] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [110-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 218, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [218-220] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-253] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-55] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-56] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-106] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-54] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-54] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-54] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>