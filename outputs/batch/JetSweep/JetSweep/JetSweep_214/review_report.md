# Play-Annotation-Generator Annotation Review — JetSweep_214

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_214`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `1` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 87 | START | 87 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `8` | `7` | 88 | START | 88 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 88 | START | 88 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 88 | START | 101 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 88 | START | 88 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 88 | START | 88 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 88 | START | 88 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `20` | `19` | 89 | START | 89 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 100 | END | 87 | 100 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 112 | START | 112 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `19` | 116 | START | 116 | 118 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 181 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 100 | 14 | inferred_complete_timeline |
| `Action_None` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_Toss` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 152 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_LeadBlock` | 88 | 157 | 70 | inferred_complete_timeline |
| `Action_LeadBlock` | 161 | 167 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 127 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 122 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 147 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 127 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 174 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 86 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 100 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 155 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 123 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 118 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 86 | 64 | inferred_complete_timeline |
| `Action_None` | 87 | 117 | 31 | inferred_complete_timeline |
| `Action_None` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 150 | 168 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 139 | 148 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 137 | 51 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 120 | 34 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 161 | 10 | inferred_complete_timeline |
| `Action_None` | 166 | 208 | 43 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 132 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 202 | 42 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 117 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 148 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 2–269 | 222 | 7 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 89–125 | 30 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 99–154 | 52 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 106–160 | 41 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 113–155 | 37 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 128–269 | 142 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 129–148 | 20 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 131–168 | 22 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 135–139 | 5 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 135–142 | 8 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 147–269 | 80 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 150–269 | 80 | 4 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 156–163 | 8 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 161–163 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 169–176 | 8 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 171–267 | 90 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 177–269 | 93 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 200–220 | 19 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 207–263 | 26 | 6 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 229–261 | 33 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 238–240 | 3 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 430: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=88, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 94 frames exceeds threshold 90 frames [start=88, end=181].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [87–100], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=101.
- ⚠️ Action 'Action_None' range [87-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-152] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-174] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [88-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [161-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-120] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-208] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-155] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-19] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [89-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-160] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-245] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-267] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-261] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>