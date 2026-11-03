# Play-Annotation-Generator Annotation Review — OutRoutes_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_38`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | Position_Unknown | Team_Unknown | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | LB1 | defense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `19` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `11` | `11` | 26 | START | 26 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `2` | `2` | 26 | START | 66 | 70 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `3` | `3` | 26 | START | 53 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 26 | START | 26 | 58 |
| ✅ EXACT | `Action_RunOutRoute` | Position_Unknown | `19` | `16` | 29 | START | 29 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | LB1 | `4` | `4` | 29 | START | 29 | 30 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 29 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `13` | `13` | 81 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `19` | `16` | 118 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `19` | `16` | 127 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 53 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 63 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 87 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 42 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 58 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 78 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 36 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 66 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 119 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 62 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 106 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 82 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunOutRoute` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_RunOutRoute` | 55 | 66 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 6–70 | 7 | 2 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 17–44 | 28 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 24–81 | 41 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 29–30 | 2 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 32–34 | 3 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 35–168 | 120 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 37–68 | 32 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 37–66 | 24 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 52–70 | 19 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 67–74 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 67–80 | 14 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 67–68 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 71–389 | 316 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 71–144 | 74 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 75–89 | 5 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 79–389 | 303 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 91–389 | 293 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 96–389 | 172 | 8 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 122–389 | 264 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 140–326 | 162 | 3 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 162–377 | 197 | 3 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 187–254 | 68 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 200–247 | 48 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 204–389 | 186 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 207–389 | 183 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 212–389 | 178 | 1 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 309–355 | 43 | 3 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 345–389 | 45 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 345–354 | 10 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 373–389 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `3` (C): Annotated start 26 != Inferred start 53
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `4` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `13` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `13` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '13' has invalid range: start=81, end=70. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '16' has invalid range: start=118, end=30. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=127, end=30. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [29-30] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [49-52] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [55-66] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-42] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-87] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [29-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-144] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-107] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-241] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-247] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-295] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-324] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-377] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-247] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-355] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-354] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>