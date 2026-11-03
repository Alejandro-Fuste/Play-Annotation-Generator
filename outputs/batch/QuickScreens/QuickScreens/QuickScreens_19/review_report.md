# Play-Annotation-Generator Annotation Review — QuickScreens_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR | offense | `0` | `0` |
| ✅ EXACT | `Action_SecureCatch` | WR | offense | `0` | `0` |
| ✅ EXACT | `Action_RunAfterCatch` | WR | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 5 | START | 5 | 8 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 8 | END | 5 | 8 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `17` | `17` | 22 | START | 22 | 34 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR | `0` | `0` | 25 | START | 25 | 44 |
| ✅ EXACT | `Action_SecureCatch` | WR | `0` | `0` | 49 | START | 49 | 56 |
| ✅ EXACT | `Action_RunAfterCatch` | WR | `0` | `0` | 61 | START | 61 | 120 |

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
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_None` | 35 | 120 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 120 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 120 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_SecureCatch` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 61 | 120 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 34 | 30 | inferred_complete_timeline |
| `Action_None` | 37 | 43 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 17 | 9 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 54 | 50 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 120 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_None` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_None` | 44 | 120 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 24 | 20 | inferred_complete_timeline |
| `Action_None` | 60 | 120 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_None` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_None` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 26 | 22 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 120 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_None` | 68 | 120 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 120 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_None` | 34 | 43 | 10 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 95 | 91 | inferred_complete_timeline |
| `Action_None` | 98 | 120 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 99 | 95 | inferred_complete_timeline |
| `Action_None` | 103 | 120 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 58 | 54 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 81 | 109 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_None` | 69 | 120 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–47 | 48 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–120 | 78 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 62–120 | 58 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 79–120 | 41 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 82–119 | 27 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 84–111 | 5 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 94–104 | 11 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 103–120 | 17 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 108–116 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 23: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 24: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_RunAfterCatch' range [61-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-44] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-17] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-120] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-54] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-37] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-26] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-120] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-97] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-103] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-116] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>