# Play-Annotation-Generator Annotation Review — DeepCross_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_109`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 176
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 142
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB1 | defense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 15 | START | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 18 | START | 18 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 18 | START | 18 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 18 | START | 30 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `5` | 18 | START | 18 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | CB1 | `11` | `11` | 29 | START | 29 | 46 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 29 | END | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `14` | `14` | 92 | START | 92 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_None` | 30 | 91 | 62 | inferred_complete_timeline |
| `Action_ThrowPass` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_ThrowPass` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 123 | 133 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 85 | 71 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 95 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 189 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 44 | 30 | inferred_complete_timeline |
| `Action_None` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 86 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 47 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 47 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 45 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 97 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 159 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 47 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 170 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 41 | 27 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_None` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 86 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_None` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_None` | 81 | 86 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 60 | 46 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 86 | 20 | inferred_complete_timeline |
| `Action_None` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_None` | 157 | 184 | 28 | inferred_complete_timeline |
| `Action_None` | 187 | 198 | 12 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 66 | 52 | inferred_complete_timeline |
| `Action_None` | 68 | 97 | 30 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 36 | 22 | inferred_complete_timeline |
| `Action_None` | 39 | 56 | 18 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_None` | 67 | 77 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 51 | 171 | 121 | inferred_complete_timeline |
| `Action_None` | 172 | 181 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_None` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 156 | 51 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 196 | 26 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_None` | 18 | 210 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 83 | 69 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 120 | 33 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–117 | 114 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–170 | 159 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 79–169 | 76 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 93–106 | 9 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 103–167 | 65 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 112–210 | 92 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 116–127 | 11 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 118–193 | 44 | 9 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 118–209 | 13 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 131–210 | 31 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 138–210 | 69 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 140–210 | 53 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 147–210 | 48 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 148–166 | 7 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 165–202 | 35 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 176–210 | 35 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 190–195 | 6 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 134 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 111: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 112: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [15–29], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=30.
- ⚠️ Action 'Action_None' range [15-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-44] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-55] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-127] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-170] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-47] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-76] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-196] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-60] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-184] for track '10' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [29-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [51-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-45] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [92-99] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-55] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-56] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-56] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-47] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-109] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-163] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-158] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-191] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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