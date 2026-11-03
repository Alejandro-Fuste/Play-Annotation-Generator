# Play-Annotation-Generator Annotation Review — OutRoutes_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_52`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_RunOutRoute` | LB1 | defense | `0` | `0` |
| ✅ EXACT | `Action_RunOutRoute` | SAF | defense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | defense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | DT2 | defense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 27 | START | 27 | 80 |
| ✅ EXACT | `Action_PassBlock` | LT | `13` | `13` | 27 | START | 27 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 27 | START | 27 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 27 | START | 27 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `2` | `2` | 27 | START | 27 | 52 |
| ✅ EXACT | `Action_RunOutRoute` | LB1 | `0` | `0` | 31 | START | 31 | 150 |
| ✅ EXACT | `Action_RunOutRoute` | SAF | `1` | `1` | 31 | START | 31 | 83 |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | `4` | `4` | 31 | START | 31 | 88 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `14` | `14` | 31 | END | 31 | 31 |
| ✅ EXACT | `Action_ThrowPass` | DT2 | `14` | `14` | 60 | START | 60 | 70 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF | `1` | `1` | 87 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF | `1` | `1` | 94 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 89 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 98 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 64 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 80 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 79 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 90 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 52 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 89 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunOutRoute` | 31 | 88 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 78 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 59 | 28 | inferred_complete_timeline |
| `Action_ThrowPass` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 80 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunOutRoute` | 31 | 150 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunOutRoute` | 31 | 83 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–92 | 88 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 68–70 | 3 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 80–150 | 71 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 84–150 | 66 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 89–149 | 61 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 98–102 | 5 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 106–150 | 45 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 113–150 | 38 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 117–148 | 30 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 123–150 | 26 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 129–150 | 15 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 137–145 | 6 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 137–142 | 6 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `1` (SAF)
- ❌ Missing segment for action `Action_BallCarry` on target `1` (SAF)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '1' has invalid range: start=87, end=83. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=94, end=83. Clamping end to start.
- ⚠️ Action 'Action_RunOutRoute' range [31-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [31-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-89] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [31-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-89] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [60-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-79] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-148] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-132] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-139] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>