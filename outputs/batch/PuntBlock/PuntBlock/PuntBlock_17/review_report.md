# Play-Annotation-Generator Annotation Review — PuntBlock_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Personal_Protector3 | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Personal_Protector1 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `18` | `18` | 19 | START | 19 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Personal_Protector3 | `15` | `15` | 33 | START | 33 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 50 | END | 50 | 50 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 70 | START | 70 | 97 |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Personal_Protector1 | `5` | `5` | 138 | START | 142 | 145 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 49 | 194 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 77 | 59 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 155 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 45 | 27 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 168 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_SecureRecovery` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 112 | 9 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BlockPunt` | 33 | 66 | 34 | inferred_complete_timeline |
| `Action_BlockPunt` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 88 | 88 | 1 | inferred_complete_timeline |
| `Action_None` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 189 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 50 | 1 | inferred_complete_timeline |
| `Action_None` | 51 | 69 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 97 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 155 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 50 | 32 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 101 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 39 | 21 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 49 | 82 | 34 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 30 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_None` | 53 | 159 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 55 | 37 | inferred_complete_timeline |
| `Action_None` | 60 | 139 | 80 | inferred_complete_timeline |
| `Action_None` | 142 | 160 | 19 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 167 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 154 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 72 | 54 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 44–45 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 60–207 | 102 | 6 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 85–86 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 86–210 | 102 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 88–130 | 35 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 105–210 | 94 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 107–115 | 9 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 108–118 | 11 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 110–210 | 73 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 117–120 | 4 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 129–210 | 82 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 129–210 | 74 | 4 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 136–210 | 71 | 3 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 137–142 | 5 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 143–210 | 44 | 4 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 146–204 | 54 | 3 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 170–203 | 34 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 197–209 | 11 | 2 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `15` (2 segments found)
- ⚠️ `Action_SecureRecovery` for actor_track_id `5` (Personal_Protector1): Annotated start 138 != Inferred start 142

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 120 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [19-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-55] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-139] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-190] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-39] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-82] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-194] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-38] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [33-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 88, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [88-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-189] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [19-30] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-97] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-181] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-114] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-160] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-190] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-190] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-167] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '38' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-178] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-203] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '43' has 2 frames without a visible bounding box.
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

</details>