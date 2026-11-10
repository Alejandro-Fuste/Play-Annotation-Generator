# Play-Annotation-Generator Annotation Review — RPO_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_245`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `18` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 44 | START | 44 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 44 | START | 45 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 44 | START | 44 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 44 | START | 44 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 44 | START | 44 | 47 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `7` | 52 | START | 52 | 71 |
| ✅ EXACT | `Action_PullBall` | QB | `7` | `7` | 72 | START | 72 | 78 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 84 | START | 84 | 91 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_PullBall` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_ThrowPass` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 92 | 166 | 75 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 128 | 86 | inferred_complete_timeline |
| `Action_None` | 131 | 167 | 37 | inferred_complete_timeline |
| `Action_None` | 169 | 195 | 27 | inferred_complete_timeline |
| `Action_None` | 202 | 209 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 131 | 89 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 129 | 87 | inferred_complete_timeline |
| `Action_None` | 133 | 167 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 121 | 79 | inferred_complete_timeline |
| `Action_None` | 125 | 166 | 42 | inferred_complete_timeline |
| `Action_None` | 171 | 179 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 91 | 48 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 54 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 81 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 129 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 81 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 122 | 80 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 187 | 19 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 81 | 39 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 99 | 16 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 124 | 21 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 195 | 35 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 81 | 39 | inferred_complete_timeline |
| `Action_None` | 84 | 93 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 79 | 37 | inferred_complete_timeline |
| `Action_None` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 100 | 58 | inferred_complete_timeline |
| `Action_None` | 106 | 129 | 24 | inferred_complete_timeline |
| `Action_None` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 155 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 129 | 87 | inferred_complete_timeline |
| `Action_None` | 131 | 184 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 191 | 149 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 72–169 | 54 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 116–141 | 21 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 120–205 | 81 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 141–154 | 13 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 151–209 | 45 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 153–161 | 6 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 167–196 | 23 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 176–210 | 35 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 185–189 | 5 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 101 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [43-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-184] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-129] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-128] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-166] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-122] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-57] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-99] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-195] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-155] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-121] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-166] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-81] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-55] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-121] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-198] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
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

</details>