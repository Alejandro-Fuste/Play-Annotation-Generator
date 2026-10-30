# Play-Annotation-Generator Annotation Review — FieldGoalBlock_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `11` | `11` | 6 | START | 6 | 17 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 32 | START | 32 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | `7` | `7` | 37 | START | 37 | 38 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PlaceBall` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_None` | 18 | 39 | 22 | inferred_complete_timeline |
| `Action_None` | 64 | 83 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_KickBall` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_None` | 38 | 187 | 150 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_None` | 38 | 93 | 56 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 64 | 33 | inferred_complete_timeline |
| `Action_None` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 95 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 69 | 38 | inferred_complete_timeline |
| `Action_None` | 81 | 189 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 210 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 127 | 96 | inferred_complete_timeline |
| `Action_None` | 131 | 149 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_None` | 32 | 63 | 32 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 72 | 91 | 20 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 202 | 87 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_BlockKick` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 48 | 82 | 35 | inferred_complete_timeline |
| `Action_None` | 84 | 153 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 112 | 81 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 210 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 42 | 90 | 49 | inferred_complete_timeline |
| `Action_None` | 98 | 159 | 62 | inferred_complete_timeline |
| `Action_None` | 164 | 192 | 29 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 12–14 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 12–210 | 175 | 8 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 25–90 | 8 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 27–209 | 172 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 30–210 | 167 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 37–38 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 52–210 | 144 | 8 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 64–210 | 119 | 5 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 80–203 | 71 | 10 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 82–210 | 122 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 83–210 | 128 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 86–171 | 61 | 8 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 100–104 | 5 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 123–194 | 61 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 138–210 | 66 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 172–174 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 142: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [32-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-187] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-192] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-189] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [37-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-112] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-39] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-83] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-93] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-64] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-17] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-209] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-70] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-101] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-203] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-154] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-114] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-194] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>