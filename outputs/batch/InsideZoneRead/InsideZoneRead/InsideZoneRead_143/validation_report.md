# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_143`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_143/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [87-127] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [121-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [134-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [152-155] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-213] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [87-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' for track '6' starts at frame 117, but the player has no visible bounding box on this frame.
> - Action 'Action_Handoff' range [117-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [120-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [129-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-241] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-248] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [87-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-274] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-246] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-244] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '23' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.