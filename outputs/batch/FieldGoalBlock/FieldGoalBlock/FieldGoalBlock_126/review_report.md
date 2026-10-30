# Play-Annotation-Generator Annotation Review — FieldGoalBlock_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_126`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 1
- **Action Segments:** 130
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `6` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_BlockKick` | Interior_Rusher5 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `6` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `6` | `6` | 11 | START | 11 | 19 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 32 | START | 32 | 37 |
| ⚠️ START CHANGED | `Action_BlockKick` | Interior_Rusher5 | `7` | `7` | 37 | START | 38 | 52 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PlaceBall` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 62 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 106 | 14 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_KickBall` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_None` | 38 | 109 | 72 | inferred_complete_timeline |
| `Action_None` | 114 | 120 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 65 | 34 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 31 | 14 | inferred_complete_timeline |
| `Action_None` | 32 | 60 | 29 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_None` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 26 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 19 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 40 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 120 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 32 | 120 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 120 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 39 | 8 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BlockKick` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 120 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_None` | 38 | 67 | 30 | inferred_complete_timeline |
| `Action_None` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_None` | 38 | 120 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 60 | 29 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 72 | 120 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 45 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 3–120 | 54 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 6–32 | 16 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 10–17 | 8 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 17–120 | 104 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 23–120 | 56 | 11 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 46–120 | 21 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 50–66 | 12 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 52–105 | 53 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 58–120 | 60 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 59–120 | 55 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 70–120 | 36 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 80–118 | 25 | 6 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 85–120 | 36 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 98–112 | 14 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 98–103 | 6 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 111–120 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `29` | 46 | 52 | 4 | 57.1% | 47, 50–51 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockKick` for actor_track_id `7` (Interior_Rusher5): Annotated start 37 != Inferred start 38

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 118 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [32-120] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-36] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-109] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-106] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [38-52] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [53-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 32, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [32-35] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-67] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-60] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-120] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 32, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [32-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-31] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-66] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-120] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-69] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-93] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-113] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-120] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '35' has 1 frames without a visible bounding box.
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