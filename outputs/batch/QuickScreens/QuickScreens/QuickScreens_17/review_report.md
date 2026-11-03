# Play-Annotation-Generator Annotation Review — QuickScreens_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | OLB2 | defense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | offense | `6` | `6` |
| ⚠️ START CHANGED | `Action_ThrowScreenPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_RunAfterCatch` | WR3 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | OLB2 | `4` | `4` | 2 | START | 2 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR2 | `0` | `0` | 15 | START | 15 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 15 | END | 2 | 15 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | `6` | `6` | 15 | START | 15 | 46 |
| ⚠️ START CHANGED | `Action_ThrowScreenPass` | QB | `15` | `15` | 33 | START | 38 | 41 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `6` | `6` | 58 | START | 58 | 63 |
| ✅ EXACT | `Action_RunAfterCatch` | WR3 | `6` | `6` | 66 | START | 66 | 132 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 42 | 150 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ScreenBlock` | 15 | 83 | 69 | inferred_complete_timeline |
| `Action_ScreenBlock` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_ScreenBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_ScreenBlock` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 131 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_None` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_SecureCatch` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 66 | 132 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 56 | 150 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 35 | 34 | inferred_complete_timeline |
| `Action_None` | 37 | 150 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 60 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 27 | 26 | inferred_complete_timeline |
| `Action_None` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 150 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 50 | 49 | inferred_complete_timeline |
| `Action_None` | 55 | 150 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 39 | 38 | inferred_complete_timeline |
| `Action_None` | 45 | 67 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 37 | 40 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 47 | 150 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 138 | 137 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 148 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 86 | 85 | inferred_complete_timeline |
| `Action_None` | 88 | 135 | 48 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–99 | 100 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 35–150 | 98 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 36–48 | 5 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 38–39 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 75–150 | 72 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 79–89 | 11 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 79–80 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 81–150 | 68 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 94–150 | 49 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 95–150 | 56 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 113–114 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 116–145 | 12 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 118–139 | 16 | 4 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 126–143 | 18 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 138–150 | 11 | 3 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ScreenBlock` and target `0` (4 segments found)
- ⚠️ `Action_ThrowScreenPass` for actor_track_id `15` (QB): Annotated start 33 != Inferred start 38

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ScreenBlock' range [15-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [86-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [97-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-48] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-150] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-22] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-28] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-148] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [66-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-37] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-60] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-150] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-89] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-143] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>