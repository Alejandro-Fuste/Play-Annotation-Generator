# Play-Annotation-Generator Annotation Review — RPO_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_61`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 145
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `3` | 44 | START | 44 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 44 | START | 45 | 47 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `18` | `18` | 44 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 44 | START | 44 | 45 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `20` | `20` | 44 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 44 | START | 45 | 47 |
| ✅ EXACT | `Action_PullBall` | QB | `3` | `3` | 53 | START | 53 | 65 |
| ✅ EXACT | `Action_ThrowPass` | QB | `3` | `3` | 87 | START | 87 | 105 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 86 | 21 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 105 | 19 | inferred_complete_timeline |
| `Action_None` | 106 | 129 | 24 | inferred_complete_timeline |
| `Action_None` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_None` | 153 | 167 | 15 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 199 | 26 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 58 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 100 | 58 | inferred_complete_timeline |
| `Action_None` | 105 | 201 | 97 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 204 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 70 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 105 | 22 | inferred_complete_timeline |
| `Action_None` | 106 | 159 | 54 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 70 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_None` | 106 | 129 | 24 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 105 | 36 | inferred_complete_timeline |
| `Action_None` | 106 | 136 | 31 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 178 | 12 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 157 | 74 | inferred_complete_timeline |
| `Action_None` | 161 | 194 | 34 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 70 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 62 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 129 | 36 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 194 | 32 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 73 | 31 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 92 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 205 | 111 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 74 | 32 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 54 | 143 | 90 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

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
<summary>CB3 — actor_track_id `10`</summary>

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
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 182 | 140 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–210 | 157 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 56–190 | 114 | 7 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 60–70 | 11 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 60–210 | 101 | 12 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 78–111 | 34 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 86–210 | 53 | 13 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 97–115 | 11 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 105–209 | 87 | 8 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 120–210 | 73 | 7 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 123–210 | 88 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 127–150 | 24 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 176–210 | 31 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 198–209 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 145 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=44, end=35. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=44, end=35. Clamping end to start.
- ⚠️ Action 'Action_None' range [43-204] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-74] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-92] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-205] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-167] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-199] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-70] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-61] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-70] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-105] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-70] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-105] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-71] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-190] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-70] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-151] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-162] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '34' has 3 frames without a visible bounding box.
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