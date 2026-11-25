# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_370`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_370/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [5–18], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=19.
> - Action 'Action_ZoneBlock' range [8-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '0' starts at frame 92, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [92-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-101] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-95] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-48] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [59-220] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-112] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '22' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_370'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.