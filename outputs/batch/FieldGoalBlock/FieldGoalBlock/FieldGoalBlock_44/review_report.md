# Play-Annotation-Generator Annotation Review — FieldGoalBlock_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | Team_Unknown | `17` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `6` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 16 | START | 16 | 31 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `6` | `6` | 32 | START | 32 | 45 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 51 | START | 51 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | `17` | `16` | 53 | START | 54 | 64 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PlaceBall` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_None` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_KickBall` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 74 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 66 | 74 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 38 | 23 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 39 | 24 | inferred_complete_timeline |
| `Action_None` | 41 | 68 | 28 | inferred_complete_timeline |
| `Action_None` | 141 | 168 | 28 | inferred_complete_timeline |
| `Action_None` | 186 | 211 | 26 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 66 | 51 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 32 | 77 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 79 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_None` | 53 | 68 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 77 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 72 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 74 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–77 | 78 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 3–68 | 44 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 28–70 | 43 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 33–68 | 32 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 35–189 | 75 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 39–44 | 6 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 42–55 | 13 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 45–70 | 25 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 53–64 | 12 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 62–66 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 84–95 | 12 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 84–95 | 12 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 88–94 | 7 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 127–135 | 9 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 139–239 | 99 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 142–239 | 91 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 142–239 | 80 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 142–239 | 90 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 142–168 | 13 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 144–153 | 7 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 146–227 | 63 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 147–239 | 93 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 147–164 | 14 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 147–239 | 92 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 164–239 | 72 | 4 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 183–239 | 42 | 3 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 187–236 | 47 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 202–218 | 9 | 2 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 220–239 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_End` position mapped to `offense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 89 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [60-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-74] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-168] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-38] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-48] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-79] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [54-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [66-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-74] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-187] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-224] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>