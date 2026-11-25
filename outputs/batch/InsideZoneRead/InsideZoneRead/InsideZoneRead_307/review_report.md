# Play-Annotation-Generator Annotation Review — InsideZoneRead_307

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_307`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | CB5 | defense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | CB5 | defense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | CB5 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB5 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | RG | `14` | `13` | 19 | START | 19 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 22 | START | 22 | 25 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 22 | START | 22 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 22 | START | 22 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 22 | START | 22 | 60 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `21` | 22 | START | 58 | 93 |
| ✅ EXACT | `Action_SnapReceive` | CB5 | `13` | `12` | 32 | END | 19 | 32 |
| ✅ EXACT | `Action_ReadDefender` | CB5 | `13` | `12` | 35 | START | 35 | 39 |
| ✅ EXACT | `Action_Keep` | CB5 | `13` | `12` | 40 | START | 40 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB5 | `13` | `12` | 64 | START | 64 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 93 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 22 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 172 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 59 | 41 | inferred_complete_timeline |
| `Action_None` | 64 | 93 | 30 | inferred_complete_timeline |
| `Action_None` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 111 | 132 | 22 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 166 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 63 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 163 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 72 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 19 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 93 | 36 | inferred_complete_timeline |
| `Action_None` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 93 | 72 | inferred_complete_timeline |
| `Action_None` | 94 | 171 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 38 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 43 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 28 | 10 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_None` | 80 | 180 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 40 | 22 | inferred_complete_timeline |
| `Action_None` | 53 | 154 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_None` | 72 | 164 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 53 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 65 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_Keep` | 40 | 63 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 180 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 30–179 | 128 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 31–161 | 126 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 33–167 | 114 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 68–172 | 105 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 93–157 | 62 | 3 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 112–180 | 68 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 22 != Inferred start 58
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 614: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [19-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-57] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-19] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-51] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-72] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-172] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-157] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_307'; source metadata written as null.

</details>