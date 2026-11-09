# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_126`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-175] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-113] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-180] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.