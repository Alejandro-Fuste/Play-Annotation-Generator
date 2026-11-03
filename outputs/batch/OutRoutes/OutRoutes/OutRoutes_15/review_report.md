# Play-Annotation-Generator Annotation Review — OutRoutes_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `13` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `10` | `10` | 9 | START | 9 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 9 | START | 9 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 9 | START | 9 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 9 | START | 9 | 10 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `7` | 9 | START | 9 | 150 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 16 | START | 16 | 150 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `9` | `9` | 16 | START | 16 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 16 | END | 16 | 16 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 68 | START | 68 | 76 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `9` | `9` | 92 | START | 92 | 100 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `9` | `9` | 101 | START | 101 | 122 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 16 | 1 | inferred_complete_timeline |
| `Action_None` | 17 | 67 | 51 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 91 | 76 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 122 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 24 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 37 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 30 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 78 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 33 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 150 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 150 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 145 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 93 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 41–42 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 58–150 | 92 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–79 | 6 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 89–150 | 62 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 114–124 | 5 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 44 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-145] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-41] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-70] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-78] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-79] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '27' has 1 frames without a visible bounding box.
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