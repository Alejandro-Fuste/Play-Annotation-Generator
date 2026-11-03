# Play-Annotation-Generator Annotation Review — QuickScreens_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowScreenPass` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 25 | START | 25 | 28 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `14` | `14` | 28 | END | 25 | 28 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | `0` | `0` | 54 | START | 54 | 77 |
| ✅ EXACT | `Action_ThrowScreenPass` | Position_Unknown | `14` | `14` | 56 | START | 56 | 64 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `0` | `0` | 83 | START | 83 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | `0` | `0` | 96 | START | 96 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 69 | 45 | inferred_complete_timeline |
| `Action_None` | 78 | 95 | 18 | inferred_complete_timeline |
| `Action_None` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 54 | 77 | 24 | inferred_complete_timeline |
| `Action_None` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_SecureCatch` | 83 | 93 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 96 | 126 | 31 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 76 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_None` | 79 | 150 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_None` | 29 | 47 | 19 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 133 | 72 | inferred_complete_timeline |
| `Action_None` | 141 | 145 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 131 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 82 | 58 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 96 | 119 | 24 | inferred_complete_timeline |
| `Action_None` | 122 | 129 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 93 | 69 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 150 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 122 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–150 | 147 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 4–150 | 119 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 93–135 | 35 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 103–146 | 33 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 116–150 | 35 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 123–150 | 23 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 124–150 | 24 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 18: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 18: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_RunAfterCatch' range [96-126] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [129-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [138-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [143-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-150] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-82] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-119] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-95] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-75] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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