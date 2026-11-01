# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `InsideZoneRead_309`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_309/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BallSnap' at frame 1 targets track ID '[?]', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [39-163] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-68] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-108] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-47] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-63] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-143] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-138] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '31' has 2 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.