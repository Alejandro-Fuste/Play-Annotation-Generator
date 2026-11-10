# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_181`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [68-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-266] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-293] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-256] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-287] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [68-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-258] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-280] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [72-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [156-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-111] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.