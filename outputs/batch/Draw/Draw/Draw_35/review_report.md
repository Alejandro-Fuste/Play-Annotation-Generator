# Play-Annotation-Generator Annotation Review — Draw_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_35`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 31 | START | 31 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `9` | 34 | START | 34 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `11` | 34 | START | 34 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `18` | 34 | START | 34 | 47 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `19` | 34 | START | 49 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 34 | START | 34 | 54 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 47 | END | 31 | 47 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `18` | `17` | 52 | START | 52 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `18` | `17` | 76 | START | 76 | 76 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 116 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 52 | 75 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 254 | 224 | inferred_complete_timeline |
| `Action_None` | 256 | 279 | 24 | inferred_complete_timeline |
| `Action_None` | 284 | 294 | 11 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 257 | 227 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 209 | 179 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 224 | 289 | 66 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 299 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 77 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 299 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 47 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 61 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 59 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 54 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_None` | 117 | 132 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 116 | 16 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 63 | 33 | inferred_complete_timeline |
| `Action_None` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 111 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 66 | 36 | inferred_complete_timeline |
| `Action_None` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_None` | 101 | 112 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 60 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 299 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 60 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 84 | 54 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 286 | 256 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 265 | 235 | inferred_complete_timeline |
| `Action_None` | 268 | 294 | 27 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 136 | 106 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 189 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 181 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 123–299 | 159 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–299 | 147 | 9 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 131–182 | 9 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 137–294 | 139 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 143–151 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 160–197 | 11 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 164–299 | 47 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 176–299 | 81 | 6 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 190–200 | 10 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 195–299 | 65 | 8 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 215–288 | 55 | 4 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 215–299 | 52 | 7 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 238–292 | 31 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 274–299 | 23 | 3 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 279–299 | 20 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 286–289 | 4 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 34 != Inferred start 49
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 122 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [31–47], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=48.
- ⚠️ Action 'Action_None' range [31-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-279] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-66] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-93] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-257] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-63] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-101] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-289] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-294] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [52-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '17' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [76-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-61] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [31-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-59] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-54] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-265] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-264] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-268] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-264] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-288] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-252] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-266] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '43' has 1 frames without a visible bounding box.
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