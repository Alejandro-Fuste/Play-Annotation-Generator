# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_283`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_283/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [1-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-208] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-133] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-67] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-151] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-204] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-68] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-167] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-163] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '31' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_283'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.