# Play-Annotation-Generator Annotation Review — PuntBlock_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_47`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockPunt` | Punter | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `16` | `16` | 12 | START | 12 | 71 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 45 | END | 45 | 45 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 72 | START | 72 | 79 |
| ✅ EXACT | `Action_BlockPunt` | Punter | `3` | `3` | 80 | START | 80 | 84 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 92 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 121 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_LongSnap` | 12 | 71 | 60 | inferred_complete_timeline |
| `Action_None` | 72 | 119 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 136 | 125 | inferred_complete_timeline |
| `Action_None` | 138 | 153 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 109 | 98 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 132 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 71 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_BlockPunt` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 128 | 39 | inferred_complete_timeline |
| `Action_None` | 130 | 187 | 58 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 159 | 148 | inferred_complete_timeline |
| `Action_None` | 169 | 202 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 38 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 183 | 172 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 88 | 77 | inferred_complete_timeline |
| `Action_None` | 93 | 203 | 111 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 69 | 58 | inferred_complete_timeline |
| `Action_None` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 148 | 37 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 26 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 34 | 23 | inferred_complete_timeline |
| `Action_None` | 36 | 81 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 115 | 104 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 136 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 156 | 13 | inferred_complete_timeline |
| `Action_None` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 156 | 145 | inferred_complete_timeline |
| `Action_None` | 160 | 210 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 68 | 57 | inferred_complete_timeline |
| `Action_None` | 72 | 138 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–77 | 75 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 11–194 | 178 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 44–210 | 165 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 50–147 | 94 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 69–77 | 9 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 98–210 | 113 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 104–108 | 4 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 112–210 | 80 | 7 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 118–199 | 30 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 134–155 | 13 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 135–150 | 16 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 143–210 | 55 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 144–210 | 52 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 151–210 | 59 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 151–164 | 14 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 88 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [12-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-37] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-132] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-202] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-138] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-121] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-183] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-69] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-148] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-203] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-144] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '38' has 1 frames without a visible bounding box.
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

</details>