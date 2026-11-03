# Play-Annotation-Generator Annotation Review — PuntBlock_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_57`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher1 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `8` | `Group` | 0 | START | 0 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `17` | `17` | 8 | START | 8 | 26 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 33 | END | 33 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `12` | `12` | 53 | START | 53 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher1 | `4` | `4` | 66 | START | 66 | 69 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 34 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_None` | 42 | 49 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 43 | 36 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_None` | 36 | 134 | 99 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 31 | 52 | 22 | inferred_complete_timeline |
| `Action_None` | 53 | 120 | 68 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 75 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 52 | 45 | inferred_complete_timeline |
| `Action_None` | 54 | 91 | 38 | inferred_complete_timeline |
| `Action_None` | 93 | 137 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 53 | 75 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 109 | 102 | inferred_complete_timeline |
| `Action_None` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_BlockPunt` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_BlockPunt` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 121 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 29 | 22 | inferred_complete_timeline |
| `Action_None` | 35 | 129 | 95 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 202 | 50 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 48 | 41 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 121 | 114 | inferred_complete_timeline |
| `Action_None` | 124 | 139 | 16 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 153 | 200 | 48 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 54 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 109 | 102 | inferred_complete_timeline |
| `Action_None` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 62 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 62 | 55 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 15–170 | 135 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 33–210 | 173 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 41–42 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 43–85 | 23 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 52–82 | 31 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 65–72 | 7 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 65–143 | 65 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 72–210 | 138 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 100–196 | 54 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 101–107 | 6 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 105–201 | 85 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 119–208 | 88 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 195–210 | 11 | 3 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 89 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-54] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [66-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-121] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-48] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-129] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [53-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [78-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-134] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [8-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-120] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-49] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-85] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-148] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-144] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '38' has 1 frames without a visible bounding box.
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

</details>