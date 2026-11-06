# Play-Annotation-Generator Annotation Review — PuntCoverage_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_42`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Left_Guard | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `19` | `19` | 1 | START | 1 | 56 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `13` | `13` | 28 | END | 28 | 28 |
| ✅ EXACT | `Action_PuntBall` | Punter | `13` | `13` | 58 | START | 58 | 73 |
| ❌ MISSING SEGMENT | `Action_CatchPunt` | Left_Guard | `12` | `12` | 204 | START | N/A | N/A |

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
- **Visible Frames:** 0–40
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 122 | 122 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 194 | 46 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 121 | 121 | inferred_complete_timeline |
| `Action_None` | 123 | 132 | 10 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 165 | 17 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 56 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |
| `Action_None` | 84 | 167 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 60 | 60 | inferred_complete_timeline |
| `Action_None` | 64 | 146 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 90 | 117 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 30 | 30 | inferred_complete_timeline |
| `Action_None` | 45 | 122 | 78 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 79 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 188 | 107 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 41 | 41 | inferred_complete_timeline |
| `Action_None` | 57 | 299 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |
| `Action_None` | 35 | 63 | 29 | inferred_complete_timeline |
| `Action_None` | 65 | 118 | 54 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 293 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 41 | 41 | inferred_complete_timeline |
| `Action_None` | 44 | 113 | 70 | inferred_complete_timeline |
| `Action_None` | 115 | 172 | 58 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 254 | 66 | inferred_complete_timeline |
| `Action_None` | 264 | 278 | 15 | inferred_complete_timeline |
| `Action_None` | 281 | 287 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 30 | 30 | inferred_complete_timeline |
| `Action_None` | 56 | 68 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 125 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 159 | 14 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 165 | 165 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 125 | 125 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 67 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 120 | 120 | inferred_complete_timeline |
| `Action_None` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 146 | 16 | inferred_complete_timeline |
| `Action_None` | 148 | 169 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 87 | 87 | inferred_complete_timeline |
| `Action_None` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 121 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 54 | 54 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 186 | 113 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |
| `Action_None` | 214 | 270 | 57 | inferred_complete_timeline |
| `Action_None` | 277 | 294 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 59–290 | 215 | 11 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 88–105 | 11 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 90–299 | 189 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 120–148 | 23 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 151–299 | 136 | 4 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 159–261 | 11 | 5 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 165–225 | 56 | 2 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 179–299 | 114 | 5 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 181–220 | 40 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 208–230 | 11 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 231–245 | 15 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 233–270 | 32 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 240–299 | 56 | 3 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 263–282 | 20 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 265–299 | 30 | 3 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 286–289 | 4 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 287–299 | 5 | 2 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 290–292 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchPunt` on target `12` (Left_Guard)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 130 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CatchPunt' for track '12' has invalid range: start=204, end=40. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-79] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-188] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-121] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-270] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-87] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-63] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-293] for track '8' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-120] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-169] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-67] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-41] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-113] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-254] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-278] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-87] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-41] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-122] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [1-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-30] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-87] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-140] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-217] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-270] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-290] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-140] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-170] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-217] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-253] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-220] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '41' has 1 frames without a visible bounding box.
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