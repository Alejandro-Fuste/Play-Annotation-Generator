# Play-Annotation-Generator Annotation Review — JetSweep_231

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_231`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 76
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE2 | defense | `10` | `9` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE2 | `10` | `9` | 1 | START | 1 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 47 | START | 47 | 61 |
| ✅ EXACT | `Action_LeadBlock` | TE | `11` | `10` | 48 | START | 48 | 133 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 48 | START | 62 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 48 | START | 48 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 48 | START | 48 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 48 | START | 48 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 48 | START | 48 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 61 | END | 47 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 66 | START | 66 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `16` | `15` | 70 | START | 70 | 207 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_Toss` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 118 | 72 | inferred_complete_timeline |
| `Action_None` | 120 | 145 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 150 | 104 | inferred_complete_timeline |
| `Action_None` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 207 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 228 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_LeadBlock` | 48 | 133 | 86 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 84 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 133 | 48 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 105 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 133 | 17 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 69 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 100 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 89 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 133 | 42 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 89 | 43 | inferred_complete_timeline |
| `Action_None` | 91 | 175 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 1 | 70 | 70 | inferred_complete_timeline |
| `Action_JetMotion` | 72 | 109 | 38 | inferred_complete_timeline |
| `Action_JetMotion` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 82 | 36 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 105 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 84 | 38 | inferred_complete_timeline |
| `Action_None` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_None` | 106 | 125 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 165 | 119 | inferred_complete_timeline |
| `Action_None` | 168 | 185 | 18 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 141 | 95 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 165 | 6 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 188 | 142 | inferred_complete_timeline |
| `Action_None` | 190 | 206 | 17 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–63 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 109–114 | 6 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 129–239 | 102 | 6 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 138–239 | 95 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 144–239 | 96 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 188–201 | 14 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 190–208 | 16 | 3 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 220–239 | 19 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `10` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 48 != Inferred start 62
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [47–61], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=62.
- ⚠️ Action 'Action_None' range [47-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-89] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-89] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-165] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-145] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-100] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [1-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [72-109] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-125] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-207] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '16' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-105] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-201] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '32' has 1 frames without a visible bounding box.
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

</details>