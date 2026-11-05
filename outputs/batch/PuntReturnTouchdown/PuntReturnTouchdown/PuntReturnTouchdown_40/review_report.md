# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_40`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 183
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 137
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `58` | `45` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 25 | START | 25 | 79 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 52 | END | 52 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `3` | `3` | 80 | START | 80 | 217 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `58` | `45` | 296 | START | 296 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 144 | 120 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 103 | 79 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 144 | 120 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LongSnap` | 25 | 79 | 55 | inferred_complete_timeline |
| `Action_None` | 80 | 279 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 253 | 229 | inferred_complete_timeline |
| `Action_None` | 257 | 286 | 30 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 88 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 103 | 79 | inferred_complete_timeline |
| `Action_None` | 106 | 131 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 79 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 80 | 217 | 138 | inferred_complete_timeline |
| `Action_PuntBall` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 182 | 158 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 167 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 53 | 29 | inferred_complete_timeline |
| `Action_None` | 55 | 299 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 41 | 107 | 67 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 142 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 46 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 73 | 49 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_None` | 49 | 99 | 51 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 56 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 169 | 145 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 144 | 120 | inferred_complete_timeline |
| `Action_None` | 147 | 182 | 36 | inferred_complete_timeline |
| `Action_None` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_None` | 199 | 212 | 14 | inferred_complete_timeline |
| `Action_None` | 214 | 221 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 40 | 16 | inferred_complete_timeline |
| `Action_None` | 42 | 282 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–213 | 213 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–164 | 123 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–167 | 158 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 63–212 | 80 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 76–299 | 217 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 76–299 | 190 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 82–83 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 91–299 | 209 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 113–118 | 6 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 120–299 | 158 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 126–181 | 12 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 128–131 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 130–157 | 27 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 139–299 | 161 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 154–299 | 146 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 157–282 | 92 | 9 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 163–166 | 4 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 165–299 | 135 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 169–299 | 131 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 170–175 | 6 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 179–235 | 37 | 3 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 186–192 | 7 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 196–297 | 94 | 4 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 196–299 | 93 | 5 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 270–292 | 12 | 4 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 276–283 | 7 | 2 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 289–294 | 5 | 2 | Undefined position; Undefined team |
| `51` | `85` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `22` (actor_track_id `22`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 118 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [25-88] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-103] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-144] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [80-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [222-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [226-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-182] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-279] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-182] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-212] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-197] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-99] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-282] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-78] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-127] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-107] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-142] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-172] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-88] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-167] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-157] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-190] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-235] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-277] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-245] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-262] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>