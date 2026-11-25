# Play-Annotation-Generator Annotation Review — InsideZoneRead_309

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_309`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | LB2 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | LB2 | defense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | LB2 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | RB | `10` | `9` | 13 | START | 13 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 16 | START | 16 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 16 | START | 16 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 16 | START | 16 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 16 | START | 16 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 16 | START | 23 | 30 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `9` | `8` | 28 | END | 13 | 28 |
| ✅ EXACT | `Action_ReadDefender` | LB2 | `9` | `8` | 30 | START | 30 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | LB2 | `9` | `8` | 36 | START | 36 | 43 |
| ✅ EXACT | `Action_BallCarry` | LB2 | `9` | `8` | 59 | START | 59 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 163 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 24 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 139 | 127 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 83 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 53 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 91 | 45 | inferred_complete_timeline |
| `Action_None` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 68 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 91 | 19 | inferred_complete_timeline |
| `Action_None` | 92 | 108 | 17 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 46 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 91 | 34 | inferred_complete_timeline |
| `Action_None` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 123 | 13 | inferred_complete_timeline |
| `Action_None` | 129 | 180 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 120 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 34 | 180 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 60 | 180 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 169 | 157 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_None` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_Keep` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_Keep` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 180 | 122 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 119 | 107 | inferred_complete_timeline |
| `Action_None` | 122 | 172 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 104 | 92 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 67 | 55 | inferred_complete_timeline |
| `Action_None` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 180 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 32–180 | 149 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 44–180 | 113 | 5 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 58–68 | 9 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 59–180 | 122 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 92–180 | 80 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 123–180 | 54 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 131–180 | 44 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 131–180 | 38 | 3 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 171–180 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [13-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [36-43] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [57-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [13-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-139] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-163] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-68] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-108] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-60] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-143] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '31' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_309'; source metadata written as null.

</details>