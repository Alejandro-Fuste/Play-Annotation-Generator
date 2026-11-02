# Play-Annotation-Generator Annotation Review — JetSweep_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 28
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | SS | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_JetMotion` | WR | `7` | `6` | 49 | START | 49 | 100 |
| ✅ EXACT | `Action_BallSnap` | SS | `13` | `12` | 73 | START | 73 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `6` | `5` | 75 | START | 75 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 75 | START | 75 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 75 | START | 75 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 75 | START | 75 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 75 | START | 75 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 75 | START | 75 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 86 | END | 73 | 86 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 92 | START | 92 | 100 |
| ✅ EXACT | `Action_BallCarry` | WR | `7` | `6` | 101 | START | 101 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `21` | `20` | 103 | START | 103 | 107 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `17` | `16` | 152 | BOUNDARY | 149 | 152 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `18` | `17` | 152 | BOUNDARY | 112 | 152 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `21` | `20` | 152 | BOUNDARY | 109 | 152 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `22` | `21` | 152 | BOUNDARY | 149 | 152 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `5` | `4` | 152 | BOUNDARY | 75 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_Toss` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 101 | 154 | 54 | inferred_complete_timeline |
| `Action_None` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 205 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 109 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 185 | 113 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_JetMotion` | 49 | 100 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 232 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_LeadBlock` | 75 | 111 | 37 | inferred_complete_timeline |
| `Action_LeadBlock` | 113 | 145 | 33 | inferred_complete_timeline |
| `Action_None` | 153 | 170 | 18 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 152 | 44 | inferred_complete_timeline |
| `Action_None` | 153 | 212 | 60 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 127 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 89 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 99 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 147 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 152 | 78 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 131 | 59 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 145 | 73 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 103 | 31 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 149 | 77 | inferred_complete_timeline |
| `Action_None` | 153 | 208 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_None` | 87 | 149 | 63 | inferred_complete_timeline |
| `Action_None` | 152 | 239 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 138 | 66 | inferred_complete_timeline |
| `Action_None` | 153 | 172 | 20 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 132 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 64–102 | 39 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 115–239 | 107 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 167–203 | 34 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 168–172 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 186–239 | 33 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 201–239 | 34 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 204–238 | 9 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 213–239 | 20 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 226–238 | 9 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 228–238 | 8 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 233–238 | 4 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [73-185] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [75-111] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [113-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-232] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-131] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-145] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-99] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-127] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-208] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [103-107] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-127] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-137] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>