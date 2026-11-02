# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_234`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '4' (TE2) duration 101 frames exceeds threshold 90 frames [start=63, end=163].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [62–77], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=78.
> - Action 'Action_None' range [62-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-129] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [63-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [133-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-224] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-141] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-219] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-206] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-232] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-235] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-157] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-224] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '40' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.