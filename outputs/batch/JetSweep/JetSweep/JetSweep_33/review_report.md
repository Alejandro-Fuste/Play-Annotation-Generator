# Play-Annotation-Generator Annotation Review — JetSweep_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 30
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | defense | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | LB | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `8` | `7` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `21` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 15 | START | 15 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 15 | START | 15 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 15 | START | 15 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 15 | START | 15 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 15 | START | 15 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 15 | START | 15 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 15 | START | 15 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 15 | START | 15 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 15 | START | 19 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `5` | `Group` | 15 | START | 15 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 15 | START | 15 | 16 |
| ✅ EXACT | `Action_JetMotion` | WR | `8` | `7` | 17 | START | 17 | 76 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | `18` | `17` | 28 | START | 28 | 141 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 49 | START | 49 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `22` | `21` | 50 | START | 58 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | LB | `15` | `14` | 50 | START | 50 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 50 | START | 63 | 63 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 50 | START | 50 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 50 | START | 50 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 50 | START | 50 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 50 | START | 50 | 74 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 62 | END | 49 | 62 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 68 | START | 68 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `8` | `7` | 77 | START | 77 | 190 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `12` | `11` | 141 | BOUNDARY | 80 | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `14` | `13` | 141 | BOUNDARY | 50 | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `16` | `15` | 141 | BOUNDARY | 78 | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `20` | `19` | 141 | BOUNDARY | N/A | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `21` | `20` | 141 | BOUNDARY | N/A | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_Toss` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 19–128
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 27 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_LeadBlock` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_LeadBlock` | 66 | 121 | 56 | inferred_complete_timeline |
| `Action_LeadBlock` | 123 | 128 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 188 | 140 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–216
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 17 | 76 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 190 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 216 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–80
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 80 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–180
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 141 | 62 | inferred_complete_timeline |
| `Action_None` | 142 | 180 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–77
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–233
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 141 | 92 | inferred_complete_timeline |
| `Action_None` | 142 | 233 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 74 | 26 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 93 | 45 | inferred_complete_timeline |
| `Action_None` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 28 | 141 | 114 | inferred_complete_timeline |
| `Action_None` | 142 | 167 | 26 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 149 | 101 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–174
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_SealBlock` | 50 | 150 | 101 | inferred_complete_timeline |
| `Action_SealBlock` | 153 | 159 | 7 | inferred_complete_timeline |
| `Action_SealBlock` | 162 | 174 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 228 | 180 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 44 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 198 | 150 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 48 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 218 | 170 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–68 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 73–191 | 118 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 87–239 | 153 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 140–239 | 84 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 163–205 | 34 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SealBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [49–62], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=63.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 92 frames exceeds threshold 90 frames [start=50, end=141].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '17' (DT) duration 114 frames exceeds threshold 90 frames [start=28, end=141].
- ⚠️ Action 'Action_None' range [49-198] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-188] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-228] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-218] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [17-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '11' starts at frame 63, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [63-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [50-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [153-159] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [162-174] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [28-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-47] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [58-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [66-121] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [123-128] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
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

</details>