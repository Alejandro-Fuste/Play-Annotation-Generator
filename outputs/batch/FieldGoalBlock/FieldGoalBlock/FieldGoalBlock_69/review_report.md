# Play-Annotation-Generator Annotation Review — FieldGoalBlock_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_69`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Left_End | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `11` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 16 | START | 16 | 25 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 42 | START | 42 | 47 |
| ✅ EXACT | `Action_BlockKick` | Left_End | `12` | `12` | 47 | START | 47 | 58 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PlaceBall` | 16 | 25 | 10 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_KickBall` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 48 | 77 | 30 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 119 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BlockKick` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 249 | 180 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 57 | 16 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 62 | 21 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_None` | 138 | 222 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 86 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 119 | 25 | inferred_complete_timeline |
| `Action_None` | 121 | 269 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 39 | 7 | inferred_complete_timeline |
| `Action_None` | 43 | 63 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_None` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 116 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 119 | 25 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 69 | 28 | inferred_complete_timeline |
| `Action_None` | 93 | 230 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 68 | 27 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 41 | 9 | inferred_complete_timeline |
| `Action_None` | 42 | 61 | 20 | inferred_complete_timeline |
| `Action_None` | 91 | 119 | 29 | inferred_complete_timeline |
| `Action_None` | 121 | 269 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_None` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 254 | 164 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 41 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 53 | 60 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 116 | 75 | inferred_complete_timeline |
| `Action_None` | 126 | 269 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 229 | 188 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_None` | 42 | 84 | 43 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 119 | 29 | inferred_complete_timeline |
| `Action_None` | 122 | 212 | 91 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 269 | 228 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `24` | Position_Unknown | Team_Unknown | 67–100 | 18 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 76–218 | 128 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 82–243 | 151 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–269 | 183 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 98–251 | 141 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 98–269 | 161 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 98–256 | 149 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 103–108 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 106–109 | 4 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 124–200 | 67 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 125–269 | 145 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 127–269 | 143 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 128–269 | 139 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 135–208 | 45 | 9 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 140–142 | 3 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 182–186 | 5 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 214–218 | 5 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 230–269 | 23 | 2 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 248–269 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 125 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [42-86] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-68] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-69] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-212] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-119] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-62] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [47-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-249] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-254] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-41] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-60] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-39] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-77] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-119] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-178] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-243] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-232] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-230] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-256] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-166] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-243] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '41' has 1 frames without a visible bounding box.
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

</details>