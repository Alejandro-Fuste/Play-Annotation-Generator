# Play-Annotation-Generator Annotation Review — PuntBlock_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_75`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `10` | `10` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Wing | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `12` | `12` | 11 | START | 11 | 21 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 33 | END | 33 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `3` | `3` | 67 | START | 67 | 131 |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | `10` | `10` | 75 | START | 75 | 83 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Wing | `4` | `4` | 195 | START | 195 | 211 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 29 | 19 | inferred_complete_timeline |
| `Action_None` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_None` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 239 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 131 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 194 | 156 | inferred_complete_timeline |
| `Action_SecureRecovery` | 195 | 211 | 17 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 66 | 41 | inferred_complete_timeline |
| `Action_None` | 67 | 189 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_None` | 134 | 212 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 66 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 131 | 65 | inferred_complete_timeline |
| `Action_PuntBall` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 75 | 65 | inferred_complete_timeline |
| `Action_None` | 78 | 130 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 111 | 101 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 45 | 35 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 227 | 176 | inferred_complete_timeline |
| `Action_None` | 230 | 236 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>? — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 179 | 169 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 220 | 210 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 47 | 222 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 22 | 12 | inferred_complete_timeline |
| `Action_None` | 61 | 181 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 18 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 198 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 92 | 82 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 127 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BlockPunt` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–239 | 184 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 17–239 | 222 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 36–42 | 7 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 45–69 | 25 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 75–157 | 80 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 79–88 | 10 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 86–220 | 133 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 96–239 | 144 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 119–121 | 3 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 155–239 | 83 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 170–173 | 4 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 178–239 | 59 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 235–238 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `?` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 152: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [11-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-92] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-227] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [134-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [11-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [26-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-222] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-212] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-69] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-111] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-157] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-220] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>