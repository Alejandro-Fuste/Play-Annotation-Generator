# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_193`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_193/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-190] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [191-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [134-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [151-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [154-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [151-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-210] for track '18' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.