# Play-Annotation-Generator Annotation Review — PuntCoverage_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_41`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 172
- **Validation Warnings:** 200
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 158
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `40` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `19` | `19` | 22 | START | 22 | 77 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 49 | END | 49 | 49 |
| ✅ EXACT | `Action_PuntBall` | Punter | `16` | `16` | 78 | START | 78 | 94 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `40` | `31` | 217 | START | 217 | 225 |

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
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 58 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 214 | 46 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 277 | 329 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 141 | 120 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 22 | 77 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 91 | 70 | inferred_complete_timeline |
| `Action_None` | 104 | 190 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 80 | 59 | inferred_complete_timeline |
| `Action_None` | 84 | 166 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 107 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 137 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 49 | 28 | inferred_complete_timeline |
| `Action_None` | 65 | 107 | 43 | inferred_complete_timeline |
| `Action_None` | 109 | 143 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 100 | 79 | inferred_complete_timeline |
| `Action_None` | 102 | 208 | 107 | inferred_complete_timeline |
| `Action_None` | 211 | 255 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 79 | 58 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 138 | 54 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 285 | 86 | inferred_complete_timeline |
| `Action_None` | 287 | 313 | 27 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 122 | 101 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 131 | 143 | 13 | inferred_complete_timeline |
| `Action_None` | 145 | 193 | 49 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 275 | 66 | inferred_complete_timeline |
| `Action_None` | 285 | 307 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 22 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 49 | 25 | inferred_complete_timeline |
| `Action_None` | 77 | 89 | 13 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 51 | 30 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 145 | 124 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 179 | 14 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 185 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 86 | 65 | inferred_complete_timeline |
| `Action_None` | 89 | 143 | 55 | inferred_complete_timeline |
| `Action_None` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 74 | 53 | inferred_complete_timeline |
| `Action_None` | 77 | 87 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 148 | 127 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 167 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 189 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 141 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 75 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–329 | 316 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 79–329 | 210 | 10 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–309 | 216 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 104–329 | 192 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 110–131 | 22 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 114–120 | 4 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 140–146 | 6 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 173–329 | 143 | 6 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 182–280 | 11 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 182–205 | 21 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 185–238 | 54 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 196–239 | 40 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 202–325 | 115 | 5 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 228–250 | 13 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 251–265 | 15 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 253–291 | 35 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 257–329 | 73 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 269–329 | 61 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 278–329 | 47 | 4 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 284–302 | 19 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 302–321 | 20 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 306–310 | 5 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 308–329 | 11 | 3 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 310–313 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 143 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [22-100] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-255] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-141] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-143] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-148] for track '6' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-189] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-190] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-79] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-313] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-122] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-143] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-275] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-107] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-86] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-62] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-179] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-107] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [22-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 22, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [22-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-122] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-160] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-289] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-317] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-231] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-291] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-309] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-131] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-314] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-205] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [217-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-244] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-325] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-280] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-302] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-321] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>