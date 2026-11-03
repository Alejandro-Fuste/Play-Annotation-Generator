# Play-Annotation-Generator Annotation Review — StopAndGo_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_51`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR1 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 5 | START | 5 | 21 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 8 | START | 8 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 8 | START | 8 | 39 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 8 | START | 22 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 8 | START | 8 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 8 | START | 8 | 70 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 21 | END | 5 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `6` | `6` | 31 | START | 31 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR1 | `6` | `6` | 62 | START | 63 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `6` | `6` | 73 | START | 73 | 141 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `17` | `17` | 84 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 76 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 59 | 55 | inferred_complete_timeline |
| `Action_None` | 63 | 83 | 21 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 91 | 168 | 78 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 196 | 19 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_VerticalStem` | 31 | 57 | 27 | inferred_complete_timeline |
| `Action_VerticalStem` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_SellStop` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_SellStop` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_RunGoRoute` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_RunGoRoute` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_RunGoRoute` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 70 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 56 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 39 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 74 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 55 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 56 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 34 | 30 | inferred_complete_timeline |
| `Action_None` | 36 | 57 | 22 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 35 | 57 | 23 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 191 | 187 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 171 | 167 | inferred_complete_timeline |
| `Action_None` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 202 | 198 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 197 | 193 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 203 | 199 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 4–210 | 207 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 94–210 | 113 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 94–210 | 95 | 9 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 102–210 | 108 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 107–124 | 7 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 109–210 | 96 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 109–129 | 21 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 109–136 | 23 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 109–113 | 5 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 109–210 | 43 | 6 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 111–210 | 81 | 8 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 135–210 | 75 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 139–210 | 57 | 5 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 152–187 | 18 | 6 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 152–200 | 17 | 5 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 187–210 | 15 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 192–210 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (5 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 8 != Inferred start 22
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SellStop` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `6` (3 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `17` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [5–21], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=22.
- ⚠️ Segment 'Action_ThrowPass' for track '17' has invalid range: start=84, end=76. Clamping end to start.
- ⚠️ Action 'Action_None' range [5-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-197] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-55] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [31-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [59-60] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellStop' range [63-68] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [73-141] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [143-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [172-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-83] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-168] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-33] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-202] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-74] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-57] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-34] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-70] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-111] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-121] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-140] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-197] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>