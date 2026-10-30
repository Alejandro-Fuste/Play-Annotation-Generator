# Play-Annotation-Generator Annotation Review — FieldGoalBlock_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_78`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Right_Edge_Rusher | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `14` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `10` | `10` | 27 | START | 27 | 45 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 64 | START | 64 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Right_Edge_Rusher | `4` | `4` | 66 | START | 66 | 74 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PlaceBall` | 27 | 45 | 19 | inferred_complete_timeline |
| `Action_None` | 46 | 161 | 116 | inferred_complete_timeline |
| `Action_None` | 170 | 198 | 29 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 71 | 140 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 80 | 88 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 126 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 95 | 32 | inferred_complete_timeline |
| `Action_None` | 99 | 124 | 26 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 191 | 59 | inferred_complete_timeline |
| `Action_None` | 193 | 200 | 8 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_None` | 64 | 201 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 97 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 63 | 14 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |
| `Action_None` | 219 | 299 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 42 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 196 | 121 | inferred_complete_timeline |
| `Action_None` | 198 | 238 | 41 | inferred_complete_timeline |
| `Action_None` | 241 | 247 | 7 | inferred_complete_timeline |
| `Action_None` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 161 | 83 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 267 | 67 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 80 | 17 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 103 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_BlockKick` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_BlockKick` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 128 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–224 | 159 | 6 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–299 | 297 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 4–133 | 29 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 25–156 | 66 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 30–166 | 137 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 49–299 | 144 | 9 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 75–218 | 86 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 95–299 | 98 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 100–105 | 6 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 106–299 | 161 | 7 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 110–299 | 171 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 111–154 | 44 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 113–299 | 175 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 113–299 | 124 | 11 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 175–200 | 24 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 237–299 | 54 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 238–299 | 57 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 264–279 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 119 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [71-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 64, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [64-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-217] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [66-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-161] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-267] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-95] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-201] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-42] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-196] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-20] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-48] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-244] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-194] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-148] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>