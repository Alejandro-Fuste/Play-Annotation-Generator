# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_15`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [139-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [166-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-225] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.