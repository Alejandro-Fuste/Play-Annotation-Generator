# Play-Annotation-Generator Annotation Review — FieldGoalBlock_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher1 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 5 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `11` | `11` | 6 | START | 6 | 16 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 19 | START | 19 | 35 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 45 | START | 45 | 49 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher1 | `13` | `13` | 49 | START | 49 | 58 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PlaceBall` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_None` | 53 | 180 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_KickBall` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_None` | 50 | 180 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 42 | 95 | 54 | inferred_complete_timeline |
| `Action_None` | 98 | 180 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 32 | 27 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 180 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 16 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 18 | 1 | inferred_complete_timeline |
| `Action_None` | 19 | 42 | 24 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 48 | 43 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 180 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 44 | 39 | inferred_complete_timeline |
| `Action_None` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 65 | 95 | 31 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 180 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 100 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_BlockKick` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 59 | 85 | 27 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 56 | 51 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_None` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 84 | 32 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 19 | 14 | inferred_complete_timeline |
| `Action_None` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 180 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 11 | 6 | inferred_complete_timeline |
| `Action_None` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 60 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 41 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 33 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_None` | 124 | 134 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 129 | 124 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 30–180 | 136 | 8 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 41–180 | 140 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 67–180 | 108 | 4 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 81–180 | 88 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 83–180 | 78 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 84–107 | 14 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 103–108 | 6 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 130–180 | 30 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 156–180 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 90 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-46] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-95] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-121] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-129] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-44] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [6-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-42] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-73] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-41] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-26] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-37] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-84] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-32] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-69] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>