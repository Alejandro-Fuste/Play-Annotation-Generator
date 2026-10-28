# Play-Annotation-Generator Annotation Review — Draw_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_86`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 125
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `16` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 22 | START | 22 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `12` | `11` | 25 | START | 25 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `13` | 25 | START | 25 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `17` | 25 | START | 25 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `20` | 25 | START | 25 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `22` | `21` | 25 | START | 45 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 36 | END | 22 | 36 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `10` | `9` | 45 | START | 45 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 71 | START | 71 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 97 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_None` | 86 | 118 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 189 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 157 | 136 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 85 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 79 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 183 | 40 | inferred_complete_timeline |
| `Action_None` | 185 | 194 | 10 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 53 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 129 | 38 | inferred_complete_timeline |
| `Action_None` | 134 | 161 | 28 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 87 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 67 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 78 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_None` | 40 | 99 | 60 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 116 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 33 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_None` | 46 | 55 | 10 | inferred_complete_timeline |
| `Action_None` | 61 | 66 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 33 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 119 | 98 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 104 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 106 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 196 | 175 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 210 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 79 | 58 | inferred_complete_timeline |
| `Action_None` | 89 | 118 | 30 | inferred_complete_timeline |
| `Action_None` | 120 | 154 | 35 | inferred_complete_timeline |
| `Action_None` | 168 | 179 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 166 | 145 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–106 | 26 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 77–210 | 103 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 81–89 | 9 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 130–210 | 74 | 4 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 136–157 | 22 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 145–210 | 58 | 4 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 149–153 | 5 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 193–210 | 17 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [22-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-118] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-99] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-87] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-157] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-66] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-79] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-79] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [22-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-129] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-89] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-183] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
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