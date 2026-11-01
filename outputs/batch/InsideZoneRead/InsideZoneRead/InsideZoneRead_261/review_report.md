# Play-Annotation-Generator Annotation Review — InsideZoneRead_261

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_261`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_Keep` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 10 | START | 10 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 13 | START | 13 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 13 | START | 13 | 40 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `19` | `18` | 13 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 13 | START | 13 | 31 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 13 | START | 13 | 77 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `19` | `18` | 24 | END | N/A | N/A |
| ✅ EXACT | `Action_ReadDefender` | C | `19` | `18` | 32 | START | 32 | 38 |
| ✅ EXACT | `Action_Keep` | C | `19` | `18` | 39 | START | 39 | 57 |
| ✅ EXACT | `Action_BallCarry` | C | `19` | `18` | 58 | START | 58 | 59 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 192 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 40 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 77 | 34 | inferred_complete_timeline |
| `Action_None` | 78 | 202 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 36 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 31 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_Keep` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 77 | 65 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 77 | 65 | inferred_complete_timeline |
| `Action_None` | 78 | 207 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 61 | 52 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 150 | 83 | inferred_complete_timeline |
| `Action_None` | 153 | 197 | 45 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 43 | 34 | inferred_complete_timeline |
| `Action_None` | 50 | 206 | 157 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 87 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_None` | 46 | 50 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 129 | 120 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 115 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 184 | 175 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 58 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 82 | 21 | inferred_complete_timeline |
| `Action_None` | 89 | 210 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 115 | 106 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 189 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 209 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 29–43 | 15 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 46–57 | 9 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 58–196 | 135 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 67–210 | 111 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 79–191 | 110 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 104–210 | 107 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 112–124 | 12 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 116–186 | 58 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 127–210 | 77 | 5 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 183–197 | 15 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (C)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=13, end=9. Clamping end to start.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=25.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_SnapReceive' annotated_start=10, effective_Action_SnapReceive_start=25.
- ⚠️ Action 'Action_None' range [10-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-61] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-150] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-197] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-120] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-192] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-87] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-207] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-184] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [32-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [39-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-202] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-157] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-157] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '33' has 1 frames without a visible bounding box.
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

</details>