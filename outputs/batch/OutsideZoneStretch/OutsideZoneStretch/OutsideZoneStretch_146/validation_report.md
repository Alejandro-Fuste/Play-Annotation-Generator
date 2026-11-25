# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_146`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_146/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
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
> - Segment 'Action_PressEdge' for track '6' has invalid range: start=108, end=73. Clamping end to start.
> - Action 'Action_PreSnap' range [0-89] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-140] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-57] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-95] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-133] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-236] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-186] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-86] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-106] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-162] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-199] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-187] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-227] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'OutsideZoneStretch_146'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.