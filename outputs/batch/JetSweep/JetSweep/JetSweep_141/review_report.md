# Play-Annotation-Generator Annotation Review — JetSweep_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_141`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_SealBlock` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR1 | `13` | `12` | 0 | START | 0 | 39 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 13 | START | 13 | 20 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 18 | START | 18 | 92 |
| ✅ EXACT | `Action_SealBlock` | RB | `15` | `14` | 19 | START | 19 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 19 | START | 19 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 19 | START | 21 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 19 | START | 19 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 19 | START | 19 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 19 | START | 19 | 26 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 20 | END | 13 | 20 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 31 | START | 31 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `13` | `12` | 40 | START | 40 | 169 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 92 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_None` | 21 | 30 | 10 | inferred_complete_timeline |
| `Action_Toss` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SealBlock` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 40 | 169 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 182 | 170 | inferred_complete_timeline |
| `Action_None` | 184 | 210 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 140 | 128 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LeadBlock` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 92 | 74 | inferred_complete_timeline |
| `Action_None` | 93 | 190 | 98 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 92 | 45 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 26 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 36 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 92 | 74 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 68 | 56 | inferred_complete_timeline |
| `Action_None` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 178 | 166 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_None` | 36 | 210 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 188 | 176 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 138 | 126 | inferred_complete_timeline |
| `Action_None` | 142 | 169 | 28 | inferred_complete_timeline |
| `Action_None` | 175 | 210 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 25–30 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 37–210 | 168 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 64–210 | 147 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 67–68 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 183–207 | 19 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 193–198 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [13–20], lower_priority='Action_ZoneBlock' annotated_start=19, effective_Action_ZoneBlock_start=21.
- ⚠️ Action 'Action_None' range [13-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [18-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-31] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [40-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [19-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-138] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-190] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-75] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '32' has 1 frames without a visible bounding box.
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