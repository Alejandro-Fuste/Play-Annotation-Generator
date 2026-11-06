# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_20`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 42: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_ZoneBlock' range [118-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-243] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [126-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [127-133] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-268] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-128] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-34] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-250] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-186] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-264] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-171] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-227] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-266] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-234] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-270] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-299] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-285] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.