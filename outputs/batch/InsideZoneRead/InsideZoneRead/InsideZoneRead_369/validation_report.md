# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_369`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_369/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 738: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [31-119] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-230] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-239] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-173] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [75-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-96] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-204] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '29' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_369'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.