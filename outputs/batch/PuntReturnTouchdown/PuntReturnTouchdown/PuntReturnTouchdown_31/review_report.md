# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_31`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 201
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 140
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `36` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `69` | `56` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 20 | START | 20 | 27 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 69 | START | 69 | 80 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `36` | `28` | 192 | START | 192 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `36` | `28` | 207 | START | 207 | 317 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `69` | `56` | 424 | START | 424 | 430 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 217 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 279 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 129 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 30 | 32 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 102 | 83 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |
| `Action_None` | 72 | 94 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_PuntBall` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_None` | 51 | 113 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 103 | 84 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 257 | 121 | inferred_complete_timeline |
| `Action_None` | 264 | 323 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 30 | 11 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_None` | 54 | 105 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 56 | 37 | inferred_complete_timeline |
| `Action_None` | 73 | 121 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 41 | 22 | inferred_complete_timeline |
| `Action_None` | 43 | 214 | 172 | inferred_complete_timeline |
| `Action_None` | 217 | 318 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 59 | 40 | inferred_complete_timeline |
| `Action_None` | 63 | 102 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 103 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 123 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 100 | 81 | inferred_complete_timeline |
| `Action_None` | 154 | 286 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–441 | 424 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 12–102 | 91 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 41–116 | 66 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 58–115 | 46 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 66–74 | 9 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–84 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 80–95 | 9 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 88–112 | 23 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 104–123 | 12 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 127–388 | 261 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 134–150 | 16 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 157–164 | 8 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 173–254 | 82 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 184–449 | 257 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 196–449 | 250 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 208–325 | 98 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 226–449 | 213 | 6 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 240–449 | 195 | 6 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 240–449 | 210 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 244–376 | 133 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 247–332 | 86 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 253–425 | 145 | 3 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 258–298 | 40 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 269–314 | 38 | 2 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 273–413 | 140 | 2 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 282–381 | 100 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 288–449 | 146 | 7 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 295–414 | 116 | 2 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 297–449 | 150 | 2 | Undefined position; Undefined team |
| `49` | `59` | Position_Unknown | Team_Unknown | 305–449 | 138 | 5 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 316–367 | 52 | 1 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 318–449 | 132 | 1 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 330–336 | 7 | 1 | Undefined position; Undefined team |
| `53` | `65` | Position_Unknown | Team_Unknown | 347–449 | 103 | 1 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 362–449 | 78 | 3 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 365–367 | 3 | 1 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 394–449 | 54 | 4 | Undefined position; Undefined team |
| `57` | `72` | Position_Unknown | Team_Unknown | 397–449 | 53 | 1 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 422–449 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `36` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 118 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [20-217] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-441] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-100] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-107] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-214] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-257] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-105] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [20-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [30-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-317] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [319-388] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-387] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-436] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-404] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-449] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-296] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-325] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-293] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-413] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-334] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-375] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-424] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-332] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-321] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-397] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-425] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-294] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-303] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-406] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-413] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-381] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-307] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-374] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-371] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-414] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-332] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-341] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-356] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-421] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-431] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-367] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-449] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-383] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-439] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-449] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>