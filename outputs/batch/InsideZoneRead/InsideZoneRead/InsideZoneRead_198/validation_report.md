# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_198`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_198/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [26-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 107, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [107-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-32] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '32' has 2 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_198'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.