# Play-Annotation-Generator Annotation Review — OutRoutes_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_60`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | RG | offense | `7` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | RG | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RG | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 15 | START | 15 | 25 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 15 | START | 15 | 60 |
| ✅ EXACT | `Action_PassBlock` | C | `17` | `17` | 15 | START | 15 | 74 |
| ✅ EXACT | `Action_PassBlock` | RG | `7` | `7` | 15 | START | 15 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `9` | `9` | 15 | START | 15 | 62 |
| ✅ EXACT | `Action_RunOutRoute` | RG | `7` | `7` | 21 | START | 21 | 65 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `19` | `18` | 21 | END | 38 | 38 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `19` | `18` | 63 | START | 63 | 72 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | RG | `7` | `7` | 101 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RG | `7` | `7` | 108 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 180 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 25 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 37 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 62 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 78 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 74 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 65 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 60 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–88 | 81 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 38–81 | 44 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 46–180 | 131 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 52–53 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 54–167 | 114 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 66–180 | 115 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 72–76 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–93 | 14 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 103–180 | 69 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 109–180 | 70 | 3 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 115–180 | 66 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 120–180 | 61 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 132–180 | 47 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 138–180 | 43 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 147–156 | 10 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `7` (RG)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '7' has invalid range: start=101, end=65. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=108, end=65. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '18' has invalid range: start=38, end=21. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [21-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-25] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-167] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-109] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-164] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-180] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-156] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>