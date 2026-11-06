# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_82`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 166: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 166: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-312] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-340] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-75] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-128] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-96] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 57, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [57-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-316] for track '10' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [319-338] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-353] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' for track '15' starts at frame 36, but the player has no visible bounding box on this frame.
> - Action 'Action_PressEdge' range [36-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-99] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-340] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-352] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-353] for track '29' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.