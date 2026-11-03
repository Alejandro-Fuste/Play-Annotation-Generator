# Play-Annotation-Generator Annotation Review — QuickScreens_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `7` | `7` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `7` | `7` | 4 | START | 4 | 16 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `3` | `3` | 16 | START | 16 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 16 | END | 4 | 16 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | `5` | `5` | 16 | START | 16 | 45 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `11` | `11` | 28 | START | 28 | 37 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `5` | `5` | 54 | START | 54 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | `5` | `5` | 77 | START | 77 | 104 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 17 | 27 | 11 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 28 | 37 | 10 | inferred_complete_timeline |
| `Action_None` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 67 | 64 | inferred_complete_timeline |
| `Action_None` | 71 | 156 | 86 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ScreenBlock` | 16 | 121 | 106 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 178 | 51 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 232 | 32 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 16 | 45 | 30 | inferred_complete_timeline |
| `Action_None` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_SecureCatch` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 77 | 104 | 28 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 108 | 125 | 18 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 128 | 158 | 31 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 166 | 235 | 70 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 32 | 29 | inferred_complete_timeline |
| `Action_None` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 215 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 105 | 102 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 150 | 22 | inferred_complete_timeline |
| `Action_None` | 168 | 186 | 19 | inferred_complete_timeline |
| `Action_None` | 191 | 218 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 55 | 52 | inferred_complete_timeline |
| `Action_None` | 57 | 113 | 57 | inferred_complete_timeline |
| `Action_None` | 135 | 162 | 28 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 239 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 105 | 102 | inferred_complete_timeline |
| `Action_None` | 108 | 125 | 18 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 17 | 43 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 177 | 174 | inferred_complete_timeline |
| `Action_None` | 180 | 191 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 213 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 109 | 106 | inferred_complete_timeline |
| `Action_None` | 114 | 120 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 156 | 29 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 106 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 140 | 137 | inferred_complete_timeline |
| `Action_None` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_None` | 163 | 191 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 145 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 224 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 14–15 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 38–239 | 202 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 48–59 | 9 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 77–78 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 123–125 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 136–239 | 101 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 177–218 | 27 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 190–211 | 22 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 212–226 | 14 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `5` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-191] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-213] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [77-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [108-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [128-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [160-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [166-235] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-43] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-125] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-218] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-162] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-215] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
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