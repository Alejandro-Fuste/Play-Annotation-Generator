# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_162`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [29-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-198] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-61] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-204] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-69] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_162'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.