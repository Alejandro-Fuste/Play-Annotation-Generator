# Play-Annotation-Generator Annotation Review — JetSweep_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_247`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 89 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `5` | `4` | 61 | START | 61 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 90 | START | 90 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | `3` | `2` | 91 | START | 91 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 91 | START | 91 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 91 | START | 91 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 91 | START | 91 | 209 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `3` | `2` | 91 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 91 | START | 103 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 102 | END | 90 | 102 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 107 | START | 107 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `4` | 116 | START | 116 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 216 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 102 | 13 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_Toss` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 299 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 281 | 192 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_JetMotion` | 61 | 115 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 218 | 103 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 235 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 299 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 185 | 96 | inferred_complete_timeline |
| `Action_None` | 188 | 205 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 252 | 163 | inferred_complete_timeline |
| `Action_None` | 287 | 291 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 35 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 89 | 49 | inferred_complete_timeline |
| `Action_None` | 90 | 128 | 39 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 82 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 209 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 90 | 102 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 166 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 209 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 209 | 119 | inferred_complete_timeline |
| `Action_LeadBlock` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 89 | 55 | inferred_complete_timeline |
| `Action_None` | 90 | 130 | 41 | inferred_complete_timeline |
| `Action_None` | 132 | 139 | 8 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 209 | 66 | inferred_complete_timeline |
| `Action_None` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 178 | 89 | inferred_complete_timeline |
| `Action_None` | 181 | 217 | 37 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 218 | 129 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 145 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |
| `Action_None` | 241 | 258 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 299 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 217 | 128 | inferred_complete_timeline |
| `Action_None` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 299 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 213 | 124 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 233 | 144 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–299 | 275 | 11 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 102–299 | 192 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 138–141 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 162–173 | 12 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 162–299 | 90 | 5 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 162–299 | 128 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 167–299 | 133 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 215–220 | 6 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 254–299 | 44 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 262–299 | 38 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 276–299 | 9 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 287–299 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 91 for track '2': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '2' (RT) duration 126 frames exceeds threshold 90 frames [start=91, end=216].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [90–102], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=103.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 126 frames exceeds threshold 90 frames [start=91, end=216].
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=91, end=82. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 126 frames exceeds threshold 90 frames [start=91, end=216].
- ⚠️ Action 'Action_None' range [90-252] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-185] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [212-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 217, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [217-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-218] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-235] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-299] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-166] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-178] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-233] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-35] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 217, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [217-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-299] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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